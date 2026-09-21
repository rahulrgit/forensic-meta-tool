# Forensic Meta Tool Pro

A privacy-focused, browser-based digital image metadata and forensic evidence indicator toolkit.

## Features

- EXIF / XMP / IPTC metadata parsing
- Camera, lens, software and timestamp fields
- GPS extraction with OpenStreetMap and Google Maps links
- SHA-256, SHA-1 and MD5 evidence hashes
- File signature / MIME consistency check
- Image dimensions and file information
- Batch image analysis
- Evidence Case ID, examiner and notes
- Forensic indicator checks
- Timestamp timeline
- JSON and CSV case export
- Printable report / Save as PDF
- Copy investigation summary
- Responsive dark forensic dashboard
- Client-side image processing; no application backend upload

## GitHub Pages

Upload `index.html` to the repository root.

Then:

Settings → Pages → Deploy from a branch → `main` → `/ (root)` → Save

Live URL:

https://rahulrgit.github.io/forensic-meta-tool/

## Important forensic limitation

This tool reports technical metadata and consistency indicators. It does **not** determine authenticity or prove that an image was manipulated. Metadata can be removed, rewritten, or legitimately changed during editing/export/copying.

## Dependencies

- Exifr via jsDelivr CDN
- SparkMD5 via jsDelivr CDN
- Web Crypto API for SHA-256/SHA-1

## License

MIT
