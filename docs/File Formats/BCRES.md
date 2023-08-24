---
date created: 2023-08-23 12:09
date updated: 2023-08-24 09:00
---

## Introduction

BCRES, which stands for "Binary CTR Resource", is a proprietary file format developed by Nintendo for the Nintendo 3DS system ("CTR" is the internal code name for the 3DS). The format is used to store a wide range of graphical assets, including 3D models, textures, animations, and other related data.

## Structure and Components

BCRES files often encapsulate several sub-files and components:

### **CMDL (3D Models)**:

Represents 3D model data, including mesh geometry, vertex data, and skeleton rigging information.

### **TEX (Textures)**:

Holds texture maps that can be applied to the 3D models. These textures can be in various formats optimized for the 3DS hardware.

### **MAAP (Material Maps)**:

Contains shading and material properties for the 3D models that determine how textures and light interact with the surface of the model.

### **Animations**:

BCRES files can also store animation data for the 3D models, such as skeleton animations, texture animations, and more.

### **Mipmaps**:

Mipmaps are integrated for texture data. Mipmaps are pre-computed, optimized sequences of images, each of which is a progressively lower resolution representation of the same texture. They improve rendering speed and reduce artifacts when textures are viewed from a distance.

### **Metadata**:

This includes various data attributes, descriptors, and additional parameters associated with the assets within the BCRES file.
