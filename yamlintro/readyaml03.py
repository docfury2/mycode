#!/usr/bin/env

def main():

    yammyfile = open("/home/student/mycode/yamlintro/myYAML.yml", "r")

    pyyammy = yaml.load(yammyfile)

    print(pyyammy)

main()
