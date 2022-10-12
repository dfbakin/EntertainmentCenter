# Entertainment Center
## The best solution to all media libraries!


Entertainment center is a simple education project for HSE. It offers convenient 

- Create or import any CSV file with the required format
- Import EntertainmentCenter class
- Launch program
- And enjoy out library


## Features

- Import a CSV file and watch it magically convert to EntertainmentCenter
- Use it in your applications free of charge (mind the GNUv3 licence)
- Browes movies in wiki
- Export documents as CSV



## Tech

Entertainment Center uses a number of open source projects to work properly:

- [wikiapi] - Python API lib to access Wiki pages
- [built-in python libs] - to work with files, generate random nums, etc.

And of course Entertainment Center itself is open source with a [public repository][dill]
 on GitHub.

## Code example

```py
    import EntertainmentCenter
    
    sample = EntertainmentCenter()
    sample.load('data/sample.csv')
    print('3 random media')
    sample.print_random_media(num_of_lines=3)
    rnd = sample.books.pick_random()
    print(type(rnd))
    rnd.name = 'New name'
    sample.save('data/new_rnd_sample.csv')
```

## Development

Want to contribute? Great!
Visit our [public repository][dill] on GitHub.


## License

GNU General Public License v3.0

**Free of charge forever!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dill]: <https://github.com/MrEmgin/EntertainmentCenter>
   [git-repo-url]: <https://github.com/MrEmgin/EntertainmentCenter.git>