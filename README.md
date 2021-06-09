# FTIRMachineLearning
 # Dependencies
 tensorflow==1.14
 
 matplotlib
 
 opencv
 
 pandas
 
 pillow
 
 cython
 
# Obtaining spectra:
Retrieving the FTIR spectra: A web scraping implementation was developed in Selenium to retrieve the FTIR spectra from the NIST Chemistry WebBook. Spectra were downloaded using the CAS number identifier in the jcamp-dx format and SMILES keys for each of the downloaded spectra were saved separately in a text file. With RDKit Python implementation, the functional groups were parsed from the spectrum’s associated key.
# Spectral processing:
After downloading the FTIR data from NIST, the following processes are completed by running the preprocess_subprocess.py script. To run this script after downloading from our GitHub, the following command line prompt should be used: “python preprocess_subprocess.py”. The script will complete eleven processes necessary to completing the training of the models.
# Creating directories on computer:
The functional group directories are created if not present in the working directory at the beginning of the subprocess script.
# Removing spectra not in absorbance or wavenumbers: 
Using the jcamp reader from github.com/nzhagen/jcamp, each downloaded FTIR spectrum is opened and read to confirm the x-axis of the trace is in wavenumber and the y-axis is in absorbance. Any spectrum that does not meet these conditions is removed from the directory. The subprocess calls on the script “check_file_in_absorbance.py”.
#Convert from jcamp-dx to csv:
Spectra in absorbance and wavenumbers are converted from jcamp-dx to csv using the jcamp reader. The subprocess calls upon the “jcamp_to_csv.py” script and completes the conversion while maintaining the original jcamp file and creating a csv file.
# Move csv files:
Using the script “move_file.py”, the csv files are moved to a new directory.
# Normalize csv files:
Each spectrum is normalized with respect to the most intense peak in the spectrum using the “normalize_csv.py” script. After normalizing, a new csv file is saved to preserve the unnormalized spectrum.
# Convert csv to jpg and move spectra images:
With the script “convert_to_jpg.py”, the normalized csv files of the spectra are converted to jpg images of the spectra. The ML method used is chosen for the image-based approach; the spectra are plotted as they would be for a chemist’s analysis. Images are moved from the directory containing the csv files for separation in the following step.
# Copy spectra images to functional group directories:
Using the SMARTS key, the functional groups for each spectrum were determined. A spectrum of a compound containing a functional group is copied to the directory for that functional group. For example, an alcohol-containing compound’s spectra is copied into the alcohol containing directory. If a compound does not contain a functional group, the spectrum is copied to the not-containing directory. 
# Test image separation and equivalent examples per class:
Five spectra from each of the containing and not containing functional groups directories are moved to a directory within the functional group directory for testing of the models after training and validation. After, the directory with more spectral images is reduced to have an equal number of images as the smaller directory. Spectra are randomly deleted from the larger directory to achieve equal examples per class.
# Model training:
Running “train_ml_subprocess.py” in the command line will train the models.
Functional group models are trained using the subprocess script to call upon and train the modified Inception V3 network for each group. The training occurs over 20,000 steps with a learning rate of 0.01. Results are saved in the functional group’s respective directory. 
# Analysis of models:
Trained model graphs and logs are opened via Tensorboard. The accuracies and cross entropies are retrieved for analysis.
# Classify:
Running “python classify_subprocess.py” in the command line classifies the segmented test images that were not used for training. The results are saved in a csv file as an accessible format.
# Pearson’s correlation coefficient:
The Pearson’s correlation coefficient is used to determine if there is a linear relationship between the number of spectra in a class and the accuracy and cross entropy in training or validation of the model. The coefficient was calculated using the SciPy “pearsonr” implementation.
# Plotting:
All plots, pie charts, and confusion matrices are plotted using Matplotlib PyPlot implementations. 
