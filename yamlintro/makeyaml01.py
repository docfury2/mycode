#!/usr/bin/python3

#yaml is not part of the standard library
import yaml

def main():
    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "Betelgeusian"}, 
            {"name": "Arthur Dent", "species": "Human"}]
    
    # display our python data
    print(hitchhikers)

    # open a new file
    zfile = open("galaxyguide.yaml", "w")

    # use the library
    ## USAGE: yaml.dump (input data, file like object)
    yaml.dump(hitchhikers, zfile)
    
    ## close the file
    zfile.close()

main()

