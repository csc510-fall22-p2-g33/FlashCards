import { Swiper, SwiperSlide } from "swiper/react";

import "swiper/css";
import "swiper/css/pagination";
import "swiper/css/navigation";

import "./styles.scss";

import { Pagination, Navigation } from "swiper";
import ReactCardFlip from "react-card-flip";
import { useState } from "react";

import JsPDF from 'jspdf';

export default function Flashcard({cards}: any) {
  

  return (
    <>
      <Swiper
        pagination={{
          type: "progressbar",
        }}
        navigation={true}
        modules={[Pagination, Navigation]}
        className="mySwiper"
      >
        {cards.map(({ front, back, hint }: any, index: number) => {
          return (
            <SwiperSlide>
              <Card
                index={index}
                total={cards.length}
                front={front}
                back={back}
              />
            </SwiperSlide>
          );
        })}
        <SwiperSlide>
          <div className="card-item final-view">
            <div>
              <p>Yaaay! You have come to the end of your practice 🎉🎊</p>
            </div>
          </div>
        </SwiperSlide>
      </Swiper>
    </>
  );
}

const Card = ({ front, back, index, total }: any) => {
  const [isFlipped, setIsFlipped] = useState(false);
  const [isLearning, setLearning] = useState(true);
  const [isBookmarked, setBookmark] = useState(false);
  async function learning (e: any) {
    if(e.target == e.currentTarget){
      e.stopPropagation()
    }
    setLearning(true);
    console.log("still learning");
  }
  async function learnt (e: any) {
    if(e.target == e.currentTarget){
      e.stopPropagation()
    }
    setLearning(false);
    console.log("learnt");
  }
  async function bookmark (e: any) {
    if(e.target == e.currentTarget){
      e.stopPropagation()
    }
    setBookmark(!isBookmarked);
    console.log("flipping bookmark");
  }

  async function generatePDF (e: any) {
    if(e.target == e.currentTarget){
      e.stopPropagation()
    }
    e.html(document.querySelector('#report')).then(() => {
      e.save('report.pdf');
  });
    console.log("downloading");
  }

  const [ourText, setOurText] = useState(front)
  const msg = new SpeechSynthesisUtterance()

  const speechHandler = (e: any) => {
    if(e.target == e.currentTarget){
      e.stopPropagation()
    }
    msg.text = ourText
    window.speechSynthesis.speak(msg)
  }
  
  return (
    <ReactCardFlip isFlipped={isFlipped} flipDirection="vertical">
      <div className="card-item" onClick={() => {
        setIsFlipped(!isFlipped)
        setOurText(back)
      }}>
        <div>
          {
              isBookmarked ?
            < input className="star-practice" type="checkbox" title="bookmark page"  style={{'backgroundColor':'green'}} onClick={bookmark}/>
            :
            < input className="star-practice" type="checkbox" title="bookmark page"  onClick={bookmark}/>
          }
          <br/><br/>
          <p>Front</p>
          <h2>{front}</h2>
          {/* tithistarts */}
          {
            isLearning ? 
            <div>
            <button style={{'marginTop': '15%', 'marginRight': '2%', 'marginBottom': '2%', 'backgroundColor':'green'}} onClick={learning}>Still learning</button>
            <button  onClick={learnt}>Learnt</button>
            </div>
            :
            <div>
            <button style={{'marginTop': '15%', 'marginRight': '2%', 'marginBottom': '2%'}} onClick={learning}>Still learning</button>
            <button  style={{'backgroundColor':'green'}} onClick={learnt}>Learnt</button>
            </div>
          }
          <button onClick={speechHandler}>Read Loud</button>
          {/* tithiends */}
        </div>
        <div className="bottom">
            <p>{index + 1} / {total}</p>
        </div>
      </div>
      <div className="card-item" onClick={() => {
        setIsFlipped(!isFlipped);
        setOurText(front)
      }}>
        <div>
          <p>Back</p>
          <h2>{back}</h2>
          <button onClick={speechHandler}>Read Loud</button>
        </div>
        <div className="bottom">
            <p>{index + 1} / {total}</p>
        </div>
      </div>
    </ReactCardFlip>
  );
};
