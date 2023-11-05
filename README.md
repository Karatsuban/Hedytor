# Hedytor
Hexadecimal editor in Python, both for local and online files


## How to use

Simply type `$ python Hedytor.py` to launch the program.

When you're in, you'll be met with a simple interface.  
There's an input line, a button and a checkBox... and that's all you need!  

### Open a file

There are several ways to open a file.  
- Type any filepath in the input line and press the button
- Click on the 'File' menu, click on 'Open file' and navigate the file browser until you found the file you want to open. Then, simply click on 'open' 
- Click on the 'File' menu, click on 'New file' and there will be a (almost) empty file just for you  
- Type a URL in the input line, check the 'Network file' checkbox and press the button  
  
Opening multiple file will create a tab for each, meaning you can have as many files open at the same time as you want!

### Save a file

Simply click on 'File', then 'Save file' and browse your folders until you found where you want to save it.

### Picture files

When you have opened a picture file, another window will open IF the picture contains EXIF data. You can view the data and choose to export them to JSON format by clicking the 'export to Json' button.  
If you've closed the window, don't worry: you can still go to the 'File' menu and chose 'export to json' from there. The little window will reappear.


### Editing the file

When a file is open, you will be met with two separate editors. When you click on one or move the cursor with the arrow keys, the selecttion will also move on the other editor. That's because the two are linked.  
To edit any data, simply type the data you want to insert and press 'Enter' when you're finished. The data will be added to both the editors.  
To delete any box, simply press the 'delete' key or the 'backspace' key.



## How does it work ?

The whole program is based on the concept of PySide6's Model-View. A model is a sort of data storage and data organizer at the same time. On top of it, there can be Views that know how to display the information the model provides. The advantages for this project are that multiple view can use the same model, so in our case, multiple editors can share the same data/file.  
Unfortunately, no Model provided by PySide6 can work exactly as we want, so I had to implement my own custom Model and write its methods to read, write or delete data.  
There are no native PySide6 View that can work out-of-the box either, so I had to use the QTableView widget. This widget displays data as a grid, so this is perfect for this editor ! No problem of alignement, all the interactions are already taken care of by the Widget itself... Right ?  
In fact, it was not that simple at all.  
For example, in one editor, we want to display the data as hexadecimal values and in the other as 'plain' alphanumerical values. But the QTableView has no method to alter the data from the Model to display it. But there exist 'delegates' object that can act as proxies between the View and the Model. In this case, the delegate assigned to the Plain Editor can modify the hexadecimal values to display them as utf-8 readable (or not) characters.  
The delegate can also allow the user to input data in the table with a custom widget instead of the limited one provided by the QTableView widget.  
So far so great, right ?  
Well, not exactly. In fact, I wanted to use the Model/View paradigm because it seemed appropriate with the goals of this dual editor and was guaranteed to remove any issue regarding duplication of data or file errors in read/write. But it made the rest _very_ difficult.  

There __are__ issues with my editor, thinks I like, things I don't, things I would like to add (see next section). In fact, I think I could achieve what I have in mind with this Model/View approach only if I was to use only Abstract Model and View and write my own classed based on those. But after making a Model more or less from scratch and learning delegates the hard way after understanding the limitations of View, I realized I had not chosen the easiest path.
Fortunately, the main program logic (opening the windows, creating tabs, opening file...) does not need to change. Only the editor part must change and could be swapped out with a working one.


## Known bugs and other irregularities

- Inserting more data than boxes left in any View does __not__ update the Views by adding rows (but the data is effectively added to the Model, as a save/reopen proves it)
- Deleting any box does not update any View until the user cliks on any View (but the Model is still updated)
- Opening any big file causes the editor to freez until both Views have created __all__ of their boxes, even the ones outside of the current viewport (in other words, this is rapidly unusable when dealing with big file)
- Opening big files can render the status bar (the bottom 'line' of the editor where some messages appear to alert on inform the user) useless and only flash a message where it is supposed to make it visible for several seconds

## What's next ?

For the time being, not much. I'm still debating whether to follow this Model/View rabbit hole all the way down and becoming a Pyside6 master along the way, or re-writing the program with a 'simpler' approach (with the default TextEdit for instance).  

But if I come back to this one day, here's a todo list of things I would like to be part of this editor:
- A search option available in each editor
- A way to control the number of columns displayed to the screen
- A way to synchronize or not the two editors (focusing on the same element at the same time or not)
- Manage the opening of big files with a little more intelligence
- Add color modes (at least a dark mode, more tired-eyes-friendly)
- Manage the save states of the file (e.g. don't close the file it has not been saved)


## Conclusion

This project really was an eye-opener on what it takes to create (and add things to) a graphical interface that is functional, easy to maintain/grow and has a simple design. It takes time, effort, planning and a bit of creativity.
