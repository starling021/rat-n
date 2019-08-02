        payload = "-c"
        cmd_data.update({"cmd":"compgen","args":payload})
        print(session.send_command(cmd_data))
