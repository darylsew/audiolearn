audiolearn
==========

A machine learning demo using PyAudio and Scikits.learn. Code here was part of a class on machine learning taught at [MIT Splash 2013](https://esp.mit.edu/learn/Splash/index.html). 

## Course Description
Machine learning is a field of computer science that concerns writing programs that can make and improve predictions or behaviors based on data inputs. The applications of machine learning are very diverse - they range from self driving cars to spam filters to autocorrect algorithms and much more. Using scikit-learn, an open source machine learning library for Python, we'll cover reinforcement learning (the kind used to create artificial intelligence for games like chess), supervised learning (the kind used in handwriting recognition), and unsupervised learning (the kind eBay uses to group its products). We'll then cover audio analysis through Fourier transforms with numpy, an open source general purpose computational library for Python, and we'll use our newfound audio analysis and machine learning skills to write very basic speech recognition software. Applications of machine learning to the fields of multitouch gesture recognition and computer vision will also be discussed, drawing from my work at Tesla and research on self driving cars and autonomous submarines.

## Documentation
Up and coming... see notes.pdf.

## Dependencies
### Audio:  
    sudo apt-get install python-pyaudio  
    sudo pip install wave  
    sudo apt-get install python-dev python-setuptools libsndfile-dev libasound2-dev  
    sudo easy_install scikits.audiolab

### Machine learning/Analysis:
    sudo pip install numpy  
    sudo pip install scipy  
    sudo pip install -U scikit-learn  

### Visualization:  
    sudo aptitude install python-qwt5-qt4  
    sudo apt-get install python-matplotlib

##Links
###Course Material
[Scikit homepage](http://scikit-learn.org/stable/)  
[Map of ML fields](http://scikit-learn.org/stable/_static/ml_map.png)  
[Cat Mouse Reinforcement Learning Demo](http://www.cse.unsw.edu.au/~cs9417ml/RL1/applet.html)  
[Self Driving Car](http://www.youtube.com/watch?v=cdgQpa1pUUE)  
[BoxCar2D Reinforcement Learning Demo](http://boxcar2d.com/about.html)  
[Vowel Classification](http://dsp.stackexchange.com/questions/8069/distinguish-vowels-from-consonants)

###Further reading/free courses
Note: I especially recommend the [Udacity AI course](https://www.udacity.com/course/cs271) for a broad introduction to the field. If you are newer to programing you should check out [CS101](https://www.udacity.com/course/cs101).  
[Derivation of Regression](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&ved=0CC4QFjAA&url=http%3A%2F%2Fseismo.berkeley.edu%2F~kirchner%2Feps_120%2FToolkits%2FToolkit_10.pdf&ei=Ry-RUtPzCuS_sQSCqYDABg&usg=AFQjCNGaKykCWw0OhYs1cWEo2ECYE2Yexg&sig2=_V-wWPAGuDC2Fsj0KcUSmQ&bvm=bv.56988011,d.cWc)  
[Good SVM Description](http://docs.opencv.org/doc/tutorials/ml/introduction_to_svm/introduction_to_svm.html)  
[Udacity Programming a Robotic Car Course](https://www.udacity.com/course/cs373)  
[Stanford Machine Learning](https://www.coursera.org/course/ml)  
