# 🕵️ Forensic Meta Tool

A privacy-focused browser-based digital image metadata and forensic evidence analyzer.

## Live on GitHub Pages

After pushing `index.html` to the repository:

**Settings → Pages → Deploy from a branch → `main` → `/ (root)` → Save**

The site will be available at:

`https://rahulrgit.github.io/forensic-meta-tool/`

## Features

- EXIF / XMP / IPTC metadata parsing
- GPS coordinates and map links
- Camera, lens, software and timestamps
- Image dimensions, MIME type and file signature
- SHA-256, SHA-1 and MD5 hashes
- Batch image analysis
- JSON and CSV export
- Print / Save as PDF
- Metadata consistency observations
- Client-side processing for privacy

> The tool reports forensic indicators. Metadata inconsistencies alone do not prove that an image was manipulated.

## Privacy

Images are processed in the browser. The application does not upload the selected image to a backend server.

The application loads Exifr and SparkMD5 from jsDelivr CDN.

## License

MIT
