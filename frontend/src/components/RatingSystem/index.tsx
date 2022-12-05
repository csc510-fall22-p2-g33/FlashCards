import React, { useState } from 'react';
import EmptyStar from '../../assets/icons/empty-star.svg';
import FilledStar from '../../assets/icons/filled-star.svg';
import http from "utils/api";
import Swal from "sweetalert2";

const Stars = ({deckid, rating}: any) => {
    const [currRating, setCurrRating] = useState(0);
    const [confirmedRating, setConfirmedRating] = useState(rating);
    const onHover = (e: any) => {
        if (e.target.className === 'star') {
            setCurrRating(e.target.dataset.value);
        }
    }
    const offHover = (e: any) => {
        setCurrRating(0);
    }
    const onClick = async(e: any) => {
        let rating = e.target.dataset.value
        if (e.target.dataset.value === confirmedRating){
            rating=rating-1;
        }
        setConfirmedRating(rating);
        await http
            .patch(`/deck/rate/${deckid}`, {'rating': rating})
            .catch((err) => {
                Swal.fire({
                icon: 'error',
                title: 'Deck Rating Failed!',
                text: 'An error occurred, please try again',
                confirmButtonColor: '#221daf',
                })
            });
    }
    return (<>
      {[0,1,2,3,4].map((index) => {
       return (<img
        onMouseOver={onHover}
        onMouseOut={offHover}
        onClick={onClick}
        data-value={index + 1}
        className="star"  
        src={index + 1 <= currRating || index + 1 <= confirmedRating ? 
            FilledStar : EmptyStar}
        alt={index + 1 <= currRating || index + 1 <= confirmedRating ? 
            "filled star" : "empty star"} />)
       })}
      </>)
  }

export default function RatingSystem({deckid, rating}: any) {
    return (
        <div>
          <Stars deckid={deckid} rating={rating}/>
        </div>
      );
}