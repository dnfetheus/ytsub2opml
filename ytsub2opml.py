import json
import sys


channel_feed_partial_url = 'https://www.youtube.com/feeds/videos.xml?channel_id='


def get_arguments() -> dict:
    if not len(sys.argv) == 3:
        print('Invalid arguments')
        exit(1)

    args = {
        'target_file': sys.argv[1],
        'generated_file': sys.argv[2]
    }

    return args


def get_channel_id(sub):
    return sub['snippet']['channelId']


def extract_channel_id(file_path):
    try:
        with open(file_path, 'r') as file:
            subs = json.load(file)
            channels_id = list(map(get_channel_id, subs))
            return channels_id

    except Exception:
        print('An error occurred while fetching the requested file')
        exit(1)



def main():
    args = validate_arguments()
    channels_id = extract_channel(args['target_file'])

if __name__ == '__main__':
    main()
    exit(0)
