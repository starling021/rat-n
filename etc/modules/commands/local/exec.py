w = os.environ['OLDPWD']
            os.chdir(w)

            session.upload_file(paths[0],remote_dir,remote_file)

            g = os.environ['HOME']
            os.chdir(g + "/mouse")
