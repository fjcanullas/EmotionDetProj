const express = require('express');
const { exec } = require('child_process');
const app = express();
const port = 5000;

// Define routes for launching different applications


app.get('/launch/3dScan', (req, res) => {
    exec('start "" "C:\\Users\\lovca\\Desktop\\3D Scan.lnk"', (error, stdout, stderr) => {
        if (error) {
            console.error(`error: ${error.message}`);
            return;
        }
        if (stderr) {
            console.error(`stderr: ${stderr}`);
            return;
        }
        console.log(`stdout: ${stdout}`);
    });

    res.send('Launching 3D Scanner...');
});

app.get('/launch/Thermalcamera', (req, res) => {
    exec('start "" "C:\\Users\\lovca\\Desktop\\3D Viewer.lnk"', (error, stdout, stderr) => {
        if (error) {
            console.log(`error: ${error.message}`);
            return;
        }
        if (stderr) {
            console.log(`stderr: ${stderr}`);
            return;
        }
        console.log(`stdout: ${stdout}`);
    });

    res.send('Launching 3d Viewer...');
});

app.get('/launch/3dviewer', (req, res) => {
    exec('start "" "C:\\Users\\lovca\\Desktop\\Kinect Studio v2.0.lnk"', (error, stdout, stderr) => {
        if (error) {
            console.log(`error: ${error.message}`);
            return;
        }
        if (stderr) {
            console.log(`stderr: ${stderr}`);
            return;
        }
        console.log(`stdout: ${stdout}`);
    });

    res.send('Launching Kinect...');
});

app.get('/launch/Skeletoncam', (req, res) => {
    exec('start "" "C:\\Users\\lovca\\Desktop\\Kinect Studio v2.0.lnk"', (error, stdout, stderr) => {
        if (error) {
            console.log(`error: ${error.message}`);
            return;
        }
        if (stderr) {
            console.log(`stderr: ${stderr}`);
            return;
        }
        console.log(`stdout: ${stdout}`);
    });

    res.send('Launching Kinect...');
});

app.get('/launch', (req, res) => {
    exec('start "" "C:\Users\lovca\Desktop\Capstone\MFTCamSysneww\MFTCamSys\emotionLauncher.bat"', (error, stdout, stderr) => {
        if (error) {
            console.log(`error: ${error.message}`);
            return;
        }
        if (stderr) {
            console.log(`stderr: ${stderr}`);
            return;
        }
        console.log(`stdout: ${stdout}`);
    });

    res.send('Launching our Emotion Detector...');
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
