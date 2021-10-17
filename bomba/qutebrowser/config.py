
# Bindings
config.bind("gi", "hint inputs")
config.bind("<f12>", "inspector")

config.unbind("+")
config.unbind("-")
config.unbind("=")
config.bind("z+", "zoom-in")
config.bind("z-", "zoom-out")
config.bind("zz", "zoom")

config.unbind("O")
config.unbind("T")
config.unbind("th")
config.unbind("tl")
config.bind("O", "set-cmd-text :open -t {url:pretty}")
config.bind("T", "set-cmd-text :open -t {url:pretty}")
config.bind("t", "set-cmd-text -s :open -t")

config.unbind("<ctrl+tab>")
config.bind("<ctrl+tab>", "tab-next")
config.bind("<ctrl+shift+tab>", "tab-prev")

config.unbind("ZQ")
config.unbind("ZZ")
config.unbind("<ctrl+q>")
config.bind("<ctrl+q>", "wq")

# Aliases for commands. The keys of the given dictionary are the
# aliases, while the values are the commands they map to.
c.aliases = {
    "w": "session-save",
    "wq": "quit --save",
    "mpv": "spawn -d mpv --force-window=immediate {url}",
    "nicehash": "spawn --userscript nicehash",
    "pass": "spawn -d pass -c",
}

# Always restore open sites when qutebrowser is reopened.
c.auto_save.session = True

# Foreground color of the URL in the statusbar on successful load
# (https).
c.colors.statusbar.url.success.https.fg = "white"

# Background color of unselected tabs.
c.colors.tabs.even.bg = "silver"
c.colors.tabs.odd.bg = "gainsboro"

# Foreground color of unselected tabs.
c.colors.tabs.even.fg = "#666666"
c.colors.tabs.odd.fg = c.colors.tabs.even.fg

# The height of the completion, in px or as percentage of the window.
c.completion.height = "20%"

# Move on to the next part when there's only one possible completion
# left.
c.completion.quick = False

# When to show the autocompletion window.
# Valid values:
#   - always: Whenever a completion is available.
#   - auto: Whenever a completion is requested.
#   - never: Never.
c.completion.show = "auto"

# Whether quitting the application requires a confirmation.
# Valid values:
#   - always: Always show a confirmation.
#   - multiple-tabs: Show a cofirmation if multiple tabs are opened.
#   - downloads: Show a confirmation if downloads are running
#   - never: Never show a confirmation.
c.confirm_quit = ["downloads"]

# Value to send in the `Accept-Language` header.
c.content.headers.accept_language = "en-US,en;q=0.8,fi;q=0.6"

# The proxy to use. In addition to the listed values, you can use a
# `socks://...` or `http://...` URL.
# Valid values:
#   - system: Use the system wide proxy.
#   - none: Don"t use any proxy
c.content.proxy = "none"

# A list of user stylesheet filenames to use.
c.content.user_stylesheets = "style.css"

# The directory to save downloads to. If unset, a sensible os-specific
# default is used.
c.downloads.location.directory = "/home/zkbturan/Downloads"

# Prompt the user for the download location. If set to false,
# `downloads.location.directory` will be used.
c.downloads.location.prompt = False

# The editor (and arguments) to use for the `open-editor` command. `{}`
# gets replaced by the filename of the file to be edited.
c.editor.command = ["kitty", "-e", "nvim '{}'"]

monospace = "8px 'Bok MonteCarlo'"

# Font used in the completion categories.
c.fonts.completion.category = f"bold {monospace}"

# Font used in the completion widget.
c.fonts.completion.entry = monospace

# Font used for the debugging console.
c.fonts.debug_console = monospace

# Font used for the downloadbar.
c.fonts.downloads = monospace

# Font used in the keyhint widget.
c.fonts.keyhint = monospace

# Font used for error messages.
c.fonts.messages.error = monospace

# Font used for info messages.
c.fonts.messages.info = monospace

# Font used for warning messages.
c.fonts.messages.warning = monospace

# Font used for prompts.
c.fonts.prompts = monospace

# Font used in the statusbar.
c.fonts.statusbar = monospace

# Font used for the hints.
c.fonts.hints = "bold 13px 'DejaVu Sans Mono'"

# Chars used for hint strings.
c.hints.chars = "asdfghjklie"

# Leave insert mode if a non-editable element is clicked.
c.input.insert_mode.auto_leave = True

# Automatically enter insert mode if an editable element is focused
# after loading the page.
c.input.insert_mode.auto_load = True

# Enable smooth scrolling for web pages. Note smooth scrolling does not
# work with the `:scroll-px` command.
c.scrolling.smooth = False

# Open new tabs (middleclick/ctrl+click) in the background.
c.tabs.background = True

# Behavior when the last tab is closed.
# Valid values:
#   - ignore: Don't do anything.
#   - blank: Load a blank page.
#   - startpage: Load the start page.
#   - default-page: Load the default page.
#   - close: Close the window.
c.tabs.last_close = "close"

# Padding around text for tabs
c.tabs.padding = {
    "left": 5,
    "right": 5,
    "top": 0,
    "bottom": 1,
}

# Which tab to select when the focused tab is removed.
# Valid values:
#   - prev: Select the tab which came before the closed one (left in horizontal, above in vertical).
#   - next: Select the tab which came after the closed one (right in horizontal, below in vertical).
#   - last-used: Select the previously selected tab.
c.tabs.select_on_remove = "prev"

# Width of the progress indicator (0 to disable).
#c.tabs.width.indicator = 0

# The page to open if :open -t/-b/-w is used without URL. Use
# `about:blank` for a blank page.
c.url.default_page = "file:///home/zkbturan/Documents/startpage/index.html"

# Definitions of search engines which can be used via the address bar.
# Maps a searchengine name (such as `DEFAULT`, or `ddg`) to a URL with a
# `{}` placeholder. The placeholder will be replaced by the search term,
# use `{{` and `}}` for literal `{`/`}` signs. The searchengine named
# `DEFAULT` is used when `url.auto_search` is turned on and something
# else than a URL was entered to be opened. Other search engines can be
# used by prepending the search engine name to the search term, e.g.
# `:open google qutebrowser`.
c.url.searchengines = {"DEFAULT": "https://duckduckgo.com/?q={}&ia=web",
                      "yt": "https://youtube.com/results?search_query={}",
                      "rd": "https://www.reddit.com/search/?q={}",
                      "aur": "https://aur.archlinux.org/packages/?O=0&SeB=nd&K={}&outdated=&SB=n%SO=a&PP=50&do_Search=Go",
                      "pamac": "https://archlinux.org/packages/?sort=&q={}&maintainer=&flagged=",
                      "wk": "https://en.wikipedia.org/w/index.pphp?search={}&title=Special%3ASearch&go=Go&ns0=1",
                      "fm": "https://www.fullhdfilmizlesene.com/arama/{}",

}
# The page(s) to open at the start.
c.url.start_pages = "file:///home/zkbturan/Documents/startpage/index.html"

# The format to use for the window title. The following placeholders are
# defined:
#   * `{perc}`: The percentage as a string like `[10%]`.
#   * `{perc_raw}`: The raw percentage, e.g. `10`
#   * `{title}`: The title of the current web page
#   * `{title_sep}`: The string ` - ` if a title is set, empty otherwise.
#   * `{id}`: The internal window ID of this window.
#   * `{scroll_pos}`: The page scroll position.
#   * `{host}`: The host of the current web page.
#   * `{backend}`: Either ''webkit'' or ''webengine''
#   * `{private}` : Indicates when private mode is enabled.
config.load_autoconfig(False)


c.content.blocking.method = 'adblock'
c.content.blocking.adblock.lists = [
        "https://easylist.to/easylist/easylist.txt",
        "https://easylist.to/easylist/easyprivacy.txt",
        "https://easylist.to/easylist/fanboy-social.txt",
        "https://secure.fanboy.co.nz/fanboy-annoyance.txt",
        "https://easylist-downloads.adblockplus.org/abp-filters-anti-cv.txt",
        "https://gitlab.com/curben/urlhaus-filter/-/raw/master/urlhaus-filter.txt",
        "https://pgl.yoyo.org/adservers/serverlist.php?showintro=0;hostformat=hosts",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/legacy.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2020.txt",
       "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2021.txt",
       "https://github.com/uBlockOrigin/uAssets/raw/master/filters/badware.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/privacy.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/badlists.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/annoyances.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/resource-abuse.txt",
        "https://www.i-dont-care-about-cookies.eu/abp/",
        "https://secure.fanboy.co.nz/fanboy-cookiemonster.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/unbreak.txt",
        "https://raw.githubusercontent.com/hectorm/hmirror/master/data/adaway.org/list.txt",
        "https://raw.githubusercontent.com/hectorm/hmirror/master/data/adblock-nocoin-list/1list.txt",
        "https://raw.githubusercontent.com/hectorm/hmirror/master/data/adguard-cname-trackers/list.txt",
        "https://raw.githubusercontent.com/hectorm/hmirror/master/data/adguard-simplified/list.txt",
        "https://raw.githubusercontent.com/hectorm/hmirror/master/data/dandelionsprout-nordic/list.txt",
        "https://raw.githubusercontent.com/hectorm/hmirror/master/data/digitalside-threat-intel/list.txt",
        "https://raw.githubusercontent.com/hectorm/hmirror/master/data/easylist/list.txt",
        "https://raw.githubusercontent.com/hectorm/hmirror/master/data/easylist-ara/list.txt",
        "https://raw.githubusercontent.com/hectorm/hmirror/master/data/easylist-bul/list.txt",
       "https://raw.githubusercontent.com/hectorm/hmirror/master/data/easylist-ces-slk/list.txt",
        "https://raw.githubusercontent.com/hectorm/hmirror/master/data/easylist-deu/list.txt",
        "https://raw.githubusercontent.com/hectorm/hmirror/master/data/easylist-fra/list.txt",
        "https://raw.githubusercontent.com/hectorm/hmirror/master/data/easylist-heb/list.txt",
        "https://raw.githubusercontent.com/hectorm/hmirror/master/data/easylist-ind/list.txt",
        "https://raw.githubusercontent.com/hectorm/hmirror/master/data/easylist-ita/list.txt",
        "https://raw.githubusercontent.com/hectorm/hmirror/master/data/easylist-kor/list.txt",
        "https://raw.githubusercontent.com/hectorm/hmirror/master/data/easylist-lav/list.txt",
        "https://raw.githubusercontent.com/hectorm/hmirror/master/data/easylist-lit/list.txt",
        "https://raw.githubusercontent.com/hectorm/hmirror/master/data/easylist-nld/list.txt",
        "https://raw.githubusercontent.com/hectorm/hmirror/master/data/easylist-por/list.txt",
        "https://raw.githubusercontent.com/hectorm/hmirror/master/data/easylist-rus/list.txt",
        "https://raw.githubusercontent.com/hectorm/hmirror/master/data/easylist-spa/list.txt",
        "https://raw.githubusercontent.com/hectorm/hmirror/master/data/easylist-zho/list.txt",
        "https://raw.githubusercontent.com/hectorm/hmirror/master/data/easyprivacy/list.txt",
        "https://raw.githubusercontent.com/hectorm/hmirror/master/data/eth-phishing-detect/list.txt",
        "https://raw.githubusercontent.com/hectorm/hmirror/master/data/gfrogeye-firstparty-trackers/list.txt",
        "https://raw.githubusercontent.com/hectorm/hmirror/master/data/hostsvn/list.txt",
        "https://raw.githubusercontent.com/hectorm/hmirror/master/data/kadhosts/list.txt",
        "https://raw.githubusercontent.com/hectorm/hmirror/master/data/matomo.org-spammers/list.txt",
        "https://raw.githubusercontent.com/hectorm/hmirror/master/data/mitchellkrogza-badd-boyz-hosts/list.txt",
        "https://raw.githubusercontent.com/hectorm/hmirror/master/data/pgl.yoyo.org/list.txt",
        "https://raw.githubusercontent.com/hectorm/hmirror/master/data/phishing.army/list.txt",
       "https://raw.githubusercontent.com/hectorm/hmirror/master/data/socram8888-notonmyshift/list.txt",
        "https://raw.githubusercontent.com/hectorm/hmirror/master/data/someonewhocares.org/list.txt",
        "https://raw.githubusercontent.com/hectorm/hmirror/master/data/spam404.com/list.txt",
        "https://raw.githubusercontent.com/hectorm/hmirror/master/data/stevenblack/list.txt",
       "https://raw.githubusercontent.com/hectorm/hmirror/master/data/ublock/list.txt",
        "https://raw.githubusercontent.com/hectorm/hmirror/master/data/ublock-abuse/list.txt",
        "https://raw.githubusercontent.com/hectorm/hmirror/master/data/ublock-badware/list.txt",
        "https://raw.githubusercontent.com/hectorm/hmirror/master/data/ublock-privacy/list.txt",
        "https://raw.githubusercontent.com/hectorm/hmirror/master/data/urlhaus/list.txt",
        "https://raw.githubusercontent.com/hectorm/hmirror/master/data/winhelp2002.mvps.org/list.txt",]
