import aiohttp
import asyncio

async def download_file(url, file_path):

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            total_size = response.content_length or 0
            chunk_size = 1024
            downloaded_size = 0

            with open(file_path, 'wb') as file:
                async for chunk in response.content.iter_chunked(chunk_size):
                    # Write the chunk to the file
                    file.write(chunk)
                    downloaded_size += len(chunk)

                    # Calculate and print the progress
                    if total_size > 0:
                        progress = (downloaded_size / total_size) * 100
                        print(f"\rDownload progress: {progress:.2f}%", end="", flush=True)

            print("\nFile downloaded successfully!")

