import { Player } from 'video-react'
import React from 'react'
import './App.css';

import "../node_modules/video-react/dist/video-react.css";

function App() {
  return (
    <div className="App">
      <div className="App-header">
        <Player
          src = "https://funtube-1259626356.cos.ap-shanghai.myqcloud.com/video/video03_diaosi_ep03.mp4"
        >
          
        </Player>
      </div>
    </div>
  );
}

export default App;
