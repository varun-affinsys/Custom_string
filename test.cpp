#include <opencv2.opencv.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>

using namespace cv;
using namespace std;

int main(){
	string path = "/home/varunsakunia/Desktop/id011.jpg";
	Mat img = imread(path);
	imshow("Image", img);
	waitKey(0);
	return 0;
}
