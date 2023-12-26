import os
import asyncio
from PIL import Image
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser

async def fix_thumb(thumb):
    width = 0
    height = 0
    try:
        if thumb is not None:
            metadata = extractMetadata(createParser(thumb))
            if metadata.has("width"):
                width = metadata.get("width")
            if metadata.has("height"):
                height = metadata.get("height")
                Image.open(thumb).convert("RGB").save(thumb)
                img = Image.open(thumb)
                img.thumbnail((320, height))  # Resizing while maintaining aspect ratio
                img.save(thumb, "JPEG")
    except Exception as e:
        print(e)
        thumb = None 
       
    return width, height, thumb

async def take_screen_shot(video_file, output_directory, ttl):
    out_put_file_name = f"{output_directory}/{time.time()}.jpg"
    file_genertor_command = [
        "ffmpeg",
        "-ss",
        str(ttl),
        "-i",
        video_file,
        "-vframes",
        "1",
        out_put_file_name
    ]
    process = await asyncio.create_subprocess_exec(
        *file_genertor_command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    e_response = stderr.decode().strip()
    t_response = stdout.decode().strip()
    if os.path.lexists(out_put_file_name):
        return out_put_file_name
    return None

# Example usage:
thumbnail_path = "path/to/thumbnail.jpg"
video_path = "path/to/video.mp4"
output_directory = "path/to/output"
thumbnail_width, thumbnail_height, resized_thumbnail = asyncio.run(fix_thumb(thumbnail_path))

if resized_thumbnail:
    screenshot_path = asyncio.run(take_screen_shot(video_path, output_directory, ttl=5))
    if screenshot_path:
        print(f"Thumbnail Size: {thumbnail_width}x{thumbnail_height}")
        print(f"Resized Thumbnail Path: {resized_thumbnail}")
        print(f"Screenshot Path: {screenshot_path}")
    else:
        print("Failed to capture screenshot.")
else:
    print("Failed to process thumbnail.")
