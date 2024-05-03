from PIL import Image
import gradio as gr
import moviepy.video.io.ImageSequenceClip


def resize_image(image: Image, size: int = 512):
    resize_img = image.resize(size)
    return resize_img


def save_gif(img_folder: list[str], fps: int = 10, loop: int = 0, resize: int = 512):

    files = [Image.open(img_path) for img_path in img_folder]
    files = [resize_image(img, (resize, resize)) for img in files]
    out_path = "gif-test.gif"
    duration = len(files) // fps

    frame_one = files[0]
    frame_one.save(
        out_path,
        format="GIF",
        append_images=files,
        save_all=True,
        duration=duration,
        loop=loop,
    )

    return out_path


def save_video(img_folder: list[str], fps: int = 10):

    out_path = "video-test.mp4"
    clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(img_folder, fps=fps)
    clip.write_videofile(out_path)

    return out_path


# Gradio Interface with Title
with gr.Blocks() as demo:
    demo.title = "Make GIF."
    demo.description = "This app creates a GIF from a folder of images."
    with gr.Row():
        with gr.Column():
            img_folder = gr.File(
                label="Select Images", file_count="multiple", height=300
            )
            with gr.Accordion("Settings"):
                fps = gr.Slider(
                    1, 61, step=10, label="Frames per second (FPS)", value=10
                )
                loop = gr.Slider(0, 10, step=1, label="Number of loops", value=0)
                resize = gr.Radio(
                    [256, 512, 1024, 2048], label="Resize images to", value=512
                )
            with gr.Row():
                gif_button = gr.Button("Create GIF")
                video_button = gr.Button("Create Video")

            
        with gr.Column():
            output_image = gr.Image(label="GIF", streaming=True)
            output_video = gr.Video(label="Video")

    gif_button.click(save_gif, [img_folder, fps, loop, resize], output_image)
    video_button.click(save_video, [img_folder, fps], output_video)

# Launch the interface
if __name__ == "__main__":
    # demo.launch(server_name="0.0.0.0")
    demo.launch()
