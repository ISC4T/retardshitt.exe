Set objShell = CreateObject("Wscript.Shell")

intMessage = Msgbox("lol", _
    vbOkOnly, "Fartnite is a virus, this is the cure")

If intMessage = vbOk Then
    objShell.Run("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
End If