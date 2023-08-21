from pytube import Playlist, YouTube
import colorama


def download_playlist(url):
    """download videos from YouTube playlist"""
    playlist = Playlist(url)
    broken_urls = []
    download_count = 1
    if playlist.videos:
        print(f'*** Download playlist to folder - {playlist.title} ***')
        for video in playlist.videos:
            try:
                print(f'Download: {download_count} / {len(playlist)} {video.title[:30]}...', end='')
                video.streams.get_highest_resolution().download(f'{playlist.title}')
                download_count += 1
                print(f'{colorama.Fore.GREEN} Done!{colorama.Fore.RESET}')
            except:
                print(f"\n{colorama.Fore.RED}(!) Something's wrong, skip: {video.title} (!){colorama.Fore.RESET}")
                broken_urls.append(video)
    else:
        print(f'{colorama.Fore.RED}URL is wrong OR playlist closed to access!{colorama.Fore.RESET}')
    if broken_urls:
        show_broken_urls(broken_urls)


def download_video(url):
    """download single video from YouTube"""
    try:
        video = YouTube(url)
        print(f'Download ...{video.title}', end='')
        video.streams.get_highest_resolution().download()
        print(f'{colorama.Fore.GREEN} ... Done!{colorama.Fore.RESET}\n')
    except:
        print(f"{colorama.Fore.RED} (!) Video from {url} can't be downloaded or wrong URL (!){colorama.Fore.RESET}\n")


def show_broken_urls(broken_urls):
    # create txt and print list of URL what can't be downloaded
    print(f"\n*** {colorama.Fore.RED}Can't download: {len(broken_urls)} {colorama.Fore.RESET}***")
    for url in broken_urls:
        print(url.watch_url, url.title)
        with open('wrong urls.txt', 'w') as er:
            er.write(f'{url.watch_url} ... {url.title}\n')
    print('Wrong urls were written to file -> wrong urls.txt\n')


def main():
    print('=== Videos will be downloaded to the current folder ===')
    print('=======================================================\n')
    while True:
        url = input('Enter the URL of a YouTube video or playlist to download (Type "q" to quit): ')
        if url == 'q':
            print('=== Thanks for using! ===')
            break
        try:
            download_playlist(url)
        except:
            download_video(url)


if __name__ == '__main__':
    main()
