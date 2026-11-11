import functools
import os
from runtime.common import asset_path, guarded, image_rgb, output_path, page_header


@functools.lru_cache(maxsize=1)
def session():
    from rembg import new_session
    model = asset_path()
    os.environ["U2NET_HOME"] = str(model.parent)
    return new_session("u2net", providers=["CPUExecutionProvider"])


@guarded
def remove_background(image, soften):
    from rembg import remove
    result = remove(image_rgb(image), session=session(), alpha_matting=bool(soften))
    destination = output_path(".png")
    result.save(destination)
    return result, str(destination)


def build_ui():
    import gradio as gr
    with gr.Blocks(title="U2Net 抠图") as ui:
        page_header()
        gr.Markdown("输出带透明通道的 PNG。复杂毛发可尝试精细边缘处理。")
        image = gr.Image(type="pil", label="原图")
        soften = gr.Checkbox(value=False, label="精细边缘处理（较慢）")
        button = gr.Button("去除背景", variant="primary")
        result = gr.Image(type="pil", image_mode="RGBA", label="透明背景结果")
        file = gr.File(label="下载透明 PNG")
        button.click(remove_background, [image, soften], [result, file], api_name="remove_background")
    return ui
