if [ "$#" -eq 0 ]; then
    echo "No arguments provided."
    exit 1
fi

if [ "$1" == "up" ]; then
    docker-compose --profile cpu up -d
elif [ "$1" == "down" ]; then
    docker-compose --profile cpu down
else
    echo "Unkown parameter: $1"
    exit 1
fi