from pystyle import Colors, Colorate
banner = '''
 █████╗ ███╗   ██╗████████╗██╗    ███████╗ ██████╗██████╗ ██╗██████╗ ████████╗    ██╗  ██╗██╗██████╗ ██████╗ ██╗
██╔══██╗████╗  ██║╚══██╔══╝██║    ██╔════╝██╔════╝██╔══██╗██║██╔══██╗╚══██╔══╝    ██║ ██╔╝██║██╔══██╗██╔══██╗██║
███████║██╔██╗ ██║   ██║   ██║    ███████╗██║     ██████╔╝██║██████╔╝   ██║       █████╔╝ ██║██║  ██║██║  ██║██║
██╔══██║██║╚██╗██║   ██║   ██║    ╚════██║██║     ██╔══██╗██║██╔═══╝    ██║       ██╔═██╗ ██║██║  ██║██║  ██║██║
██║  ██║██║ ╚████║   ██║   ██║    ███████║╚██████╗██║  ██║██║██║        ██║       ██║  ██╗██║██████╔╝██████╔╝██║
╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝        ╚═╝       ╚═╝  ╚═╝╚═╝╚═════╝ ╚═════╝ ╚═╝                                                                                                                                                       
'''

def vivod_logo():
    print(Colorate.Horizontal(Colors.yellow_to_red, banner, 1))
