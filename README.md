## CS1430 Final

This project is a reimplementation of the the [following paper](https://arxiv.org/pdf/2002.05638.pdf) on Image to Illustration translation using GANs for Brown's CS1430
Computer Vision course, created in Spring 2021. 


The data for this model can be found [here](https://github.com/artset/cs1430-final-data)


#### TODO
- [x] GCP set up VM + Buckets [Katherine]
- [ ] Preprocessing 
  - [ ] Scrape illustration data from OpenLibrary [Zoe, Liyaan]
  - [x] Get landscape data from CycleGAN dataset/Kaggle [Zoe, Liyaan]
  - [x] Scrape Miyazaki images from Google Images [Minna, Katherine]
  - [ ] Write preprocessing script to prepare images for model 
- [ ] Model 
  - [ ] Write script to run pipeline
  - [ ] Set up tensorboard
  - [ ] Model architecture
    - [ ] Generator
    - [ ] Discriminator
    - [ ] Ganilla model that puts everything together
- Project 1 Report [all]
