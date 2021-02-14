import json
import sys
import logging as logger


CHANNEL_FEED_PARTIAL_URL = 'https://www.youtube.com/feeds/videos.xml?channel_id='


def get_arguments() -> dict:
    if not len(sys.argv) == 3:
        logger.info('Invalid arguments')
        exit(1)

    args = {
        'target_file': sys.argv[1],
        'generated_file': sys.argv[2]
    }

    return args


def extract_channel_id(file_path) -> list:
    try:
        with open(file_path, 'r') as file:
            subs = json.load(file)
            channels_id = list(map(lambda sub: sub['snippet']['channelId'], subs))
            return channels_id

    except Exception:
        logger.error('An error occurred while fetching the requested file')
        exit(1)


def generate_opml(channels_id: list) -> None:
    logger.warn('TODO')


def main():
    args = get_arguments()
    channels_id = extract_channel_id(args['target_file'])
    generate_opml(channels_id)


if __name__ == '__main__':
    logger.basicConfig(level=logger.INFO)
    main()
