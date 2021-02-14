# ytsub2opml

## About

This script takes a JSON file containing a list of Youtube [subscriptions](https://developers.google.com/youtube/v3/docs/subscriptions) and generates an OPML subscription file based on its data.

You can get a list of your subscriptions by requesting it on [Google Takeout](https://takeout.google.com/settings/takeout) or requesting it to [this endpoint](https://developers.google.com/youtube/v3/docs/subscriptions/list). Personally I would recommend to use that endpoint, given that Google Takeout already uses Youtube Data API and its standard params can lead to [inaccurate data](https://stackoverflow.com/questions/32832120/max-subscribers-returned-and-duplicates-youtube-api).

Talking about use cases, the definitive one would be exporting Youtube subscriptions to a feed reader, where an OPML file would make that process much more easier.

## License

[LICENSE](./LICENSE)