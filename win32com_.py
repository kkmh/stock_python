## win32 only

import win32com.client

explore = win32com.client.Dispatch("InternetExplorer.Application")
explore.Visible = True

import win32com.client

word = win32com.client.Dispatch("Word.Application")
word.Visible = True


