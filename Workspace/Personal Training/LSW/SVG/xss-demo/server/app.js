const express = require('express');
const multer = require('multer');
const path = require('path');
const app = express();
const PORT = 3000;

// 정적 파일 제공
app.use(express.static(path.join(__dirname, 'public'))); // 'public' 폴더를 정적 파일로 사용

// Multer 설정: 업로드 파일 저장 경로 및 파일 이름 설정
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, 'uploads/'); // 업로드 디렉토리 지정
  },
  filename: (req, file, cb) => {
    cb(null, `${Date.now()}-${file.originalname}`); // 파일 이름 설정
  },
});

const upload = multer({ storage: storage });

// 메인 페이지 라우트
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html')); // index.html 경로 제공
});

// 파일 업로드 처리
app.post('/upload', upload.single('file'), (req, res) => {
  if (!req.file) {
    return res.status(400).send('파일이 업로드되지 않았습니다.');
  }
  res.send(`
    <h1>업로드 성공</h1>
    <p>파일 이름: ${req.file.originalname}</p>
    <p>저장 위치: <a href="/uploads/${req.file.filename}" target="_blank">${req.file.filename}</a></p>
    <a href="/">돌아가기</a>
  `);
});

// 서버 실행
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});