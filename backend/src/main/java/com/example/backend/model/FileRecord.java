package com.example.backend.model;

import jakarta.persistence.*;
import java.time.LocalDateTime;

@Entity
public class FileRecord {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String filename;
    private String result;

    @Column(name = "timestamp")  // ✅ Map to SQL column named 'timestamp'
    private LocalDateTime uploadedAt;

    public FileRecord() {}

    public FileRecord(String filename, String result, LocalDateTime uploadedAt) {
        this.filename = filename;
        this.result = result;
        this.uploadedAt = uploadedAt;
    }

    // Getters and setters
    public Long getId() {
        return id;
    }

    public String getFilename() {
        return filename;
    }

    public String getResult() {
        return result;
    }

    public LocalDateTime getUploadedAt() {
        return uploadedAt;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public void setFilename(String filename) {
        this.filename = filename;
    }

    public void setResult(String result) {
        this.result = result;
    }

    public void setUploadedAt(LocalDateTime uploadedAt) {
        this.uploadedAt = uploadedAt;
    }
}
