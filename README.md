audiolearn
==========

A machine learning demo using PyAudio and Scikits.  

## Course Description
Machine learning is a field of computer science that concerns writing programs that can make and improve predictions or behaviors based on some data. The applications of machine learning are very diverse -  they range from self driving cars to spam filters to autocorrect algorithms and much more. Using scikits-learn, an open source machine learning library for Python, we'll cover reinforcement learning (the kind used to create artificial intelligence for games like chess), supervised learning (the kind used in handwriting recognition), and unsupervised learning (the kind eBay uses to group its products). We'll then cover audio analysis through Fourier transforms with numpy, an open source general purpose computational library for Python, and we'll use our newfound audio analysis and machine learning skills to write very basic speech recognition software.

## Dependencies
### Audio:  
sudo apt-get install python-pyaudio  
sudo pip install wave  

### Machine learning:
sudo pip install numpy  
sudo pip install scipy  
sudo pip install -U scikit-learn  

### Visualization:  
sudo aptitude install python-qwt5-qt4
sudo apt-get install python-matplotlib

## To Do  
- [x] Record audio  
- [x] Playback audio  
- [x] Provide audio visualization for clarity (either with playback or during recording) 
- [x] Select machine learning technique  
- [ ] Record audio samples
- [ ] Extract features from audio  
- [ ] Implement machine learning technique  
- [ ] Select best features
- [ ] Observe accuracy metrics
- [ ] Real time
