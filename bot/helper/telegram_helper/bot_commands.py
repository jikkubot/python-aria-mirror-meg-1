class _BotCommands:
    def __init__(self):
        self.StartCommand = 'start'
        self.MirrorCommand = 'mirror'
        self.TarMirrorCommand = 'tarmirror'
        self.CancelMirror = 'cancel'
        self.CancelAllCommand = 'cancelall'
        self.ListCommand = 'find'
        self.StatusCommand = 'status'
        self.AuthorizeCommand = 'auth'
        self.UnAuthorizeCommand = 'unauth'
        self.PingCommand = 'ping'
        self.StatsCommand = 'serverinfo'
        self.HelpCommand = 'nohelp'
        self.LogCommand = 'log'
        self.CloneCommand = "clone"
        self.WatchCommand = 'watch'
        self.TarWatchCommand = 'tarwatch'

BotCommands = _BotCommands()
