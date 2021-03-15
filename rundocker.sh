#!/bin/bash
#set -x

python_image="tagcounter-docker"

for line in $(sudo docker images); do
   testimagename=$(echo $line | cut -d" " -f1);
   if [[ ${testimagename} == ${python_image} ]]; then
      filexists="true"
   fi
done


if [[ $filexists != "true" ]]; then
  sudo docker build --tag tagcounter-docker .
fi

#sudo docker images
## run this command in command line
# sudo docker run --rm -v $(pwd):/app tagcounter-docker python tagcounter.py #URL
echo $(pwd)

# sudo docker rmi ${python_image}
# sudo docker image -a
