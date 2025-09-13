package com.example.backend.service;

import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;

@Service
public class FileService {

    private static final String Y_DIR = "y/";
    private static final String PYTHON_SCRIPT = "face_matcher.py";

    public String processUploadedFile(MultipartFile multipartFile) {
        try {
            // Save file to y/ directory
            File file = new File(Y_DIR + multipartFile.getOriginalFilename());
            try (FileOutputStream fos = new FileOutputStream(file)) {
                fos.write(multipartFile.getBytes());
            }

            // Call Python script
            ProcessBuilder processBuilder = new ProcessBuilder("python3", PYTHON_SCRIPT, file.getPath());
            processBuilder.redirectErrorStream(true);
            Process process = processBuilder.start();

            // Read result
            java.util.Scanner scanner = new java.util.Scanner(process.getInputStream()).useDelimiter("\\A");
            String output = scanner.hasNext() ? scanner.next().trim() : "No output";
            scanner.close();

            return output;

        } catch (IOException e) {
            e.printStackTrace();
            return "Error: " + e.getMessage();
        }
    }
}
