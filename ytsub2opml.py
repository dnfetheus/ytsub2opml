import json
import sys
import logging as logger


YOUTUBE_URL = 'https://www.youtube.com/'
CHANNEL_FEED_PARTIAL_URL = 'https://www.youtube.com/feeds/videos.xml?channel_id='

OPML_TEMPLATE = '''<?xml version="1.0" encoding="UTF-8"?>
<opml version="1.0">
    <head>
        <title>Youtube subscriptions converted to OPML by ytsub2opml</title>
    </head>
    <body>
        <outline text="/yt/" title="/yt/">
            {}
        </outline>
    </body>
</opml>
'''
OUTLINE_TEMPLATE = '<outline text="{}" title="{}" type="rss" xmlUrl="{}" htmlUrl="{}"/>'

DEFAULT_OPML_FILE_PATH = 'subscriptions.xml'


def get_arguments() -> dict:
    logger.info('Validating arguments')

    if len(sys.argv) < 2:
        logger.error('Invalid arguments')
        exit(1)

    args = {
        'input_file_path': sys.argv[1],
        'output_file_path': DEFAULT_OPML_FILE_PATH if len(sys.argv) < 3 else sys.argv[2]
    }

    return args


def extract_channels(file_path: str) -> list:
    logger.info('Extracting content from Youtube subscriptions file')

    try:
        with open(file_path, 'r') as file:
            channels = list(json.load(file))
            channels.sort(key=lambda x: x['snippet']['title'].lower())

            return channels

    except:
        logger.error('An error occurred while fetching file')
        exit(1)


def to_outline(channel: dict) -> str:
    channel_id = channel['snippet']['resourceId']['channelId']
    channel_name = channel['snippet']['title']

    channel_feed_url = f'{CHANNEL_FEED_PARTIAL_URL}{channel_id}'

    return OUTLINE_TEMPLATE.format(
        channel_name, 
        channel_name, 
        channel_feed_url, 
        YOUTUBE_URL
    )


def generate_opml(channels: list, generated_file: str) -> None:
    logger.info('Generating OPML file')

    outlines = '\n            '.join(map(to_outline, channels))
    content = OPML_TEMPLATE.format(outlines)

    try:
        with open(generated_file, 'w') as file:
            file.write(content)

    except:
        logger.error('An error occurred while saving the generated file')
        exit(1)

    logger.info('OPML file has been generated successfully')


def main():
    args = get_arguments()
    channels = extract_channels(args['input_file_path'])
    generate_opml(channels, args['output_file_path'])


if __name__ == '__main__':
    logger.basicConfig(level=logger.INFO)
    main()
