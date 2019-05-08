#!/usr/bin/env

# yaml is NOT part of the standard library
import yaml

def main():
    # create a blob of data to work with
    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "Betelgeusian"},
            {"name": "Arthur Dent", "species": "Human"}]

    #display our python data
    print(hitchhikers)

    # Create the yaml string
    yamlstring = yaml.dump(hitchhikers)

    # display a single string of YAML
    print(yamlstring)

main()
