#include <iostream>

#include "cv.h"
#include "opencv2/core/core.hpp"
#include "opencv2/opencv.hpp"
#include <opencv2/aruco.hpp>

using namespace std;
using namespace cv;

int main()
{
    //1. generate marker
    int markerID = 23;
    int markerSize = 200;
    int borderSize = 1;

    cv::Mat markerImage;
    cv::aruco::Dictionary dictionary = cv::aruco::getPredefinedDictionary(cv::aruco::DICT_5X5_1000);
    cv::aruco::drawMarker(dictionary, markerID, markerSize, markerImage, borderSize);

    //showmarker
    cv::imshow("shit",markerImage);
    cv::waitKey(0);

    //2. detection of marker

    //init variables
    vector< int> markerIds;
    vector< vector<Point2f> > markerCorners, rejectedCandidates;

    //cam param
    double intrisic_matrix[3][3] = {{612.841064, 0, 323.639099}, {0, 618.606079, 233.179459}, {0, 0, 1}};
    double distortion_matrix[4] = {0,0,0,0};
    Mat cameraMatrix = Mat(3, 3, CV_64FC1, intrisic_matrix);
    Mat distCoeffs = Mat(1, 4, CV_64FC1, distortion_matrix);
    //markersize in meter
    float fMarkerLength = 0.08;
    aruco::DetectorParameters parameters;

    cv::VideoCapture Cap(0);
    cv::Mat ImageInput;

    while(Cap.grab())
    {
        Cap>>ImageInput;
        aruco::detectMarkers(ImageInput, dictionary, markerCorners, markerIds, parameters, rejectedCandidates);
        //get R and T
        if(markerIds.size()>0)
        {
            vector< Vec3d > rvecs, tvecs;
            aruco::estimatePoseSingleMarkers(markerCorners, fMarkerLength, cameraMatrix, distCoeffs, rvecs, tvecs);

        }

    }

    return 0;
}
