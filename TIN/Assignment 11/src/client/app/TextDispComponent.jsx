import React from 'react';

const TextDisp = function(props){
    return <span className={props.class}> {props.text} </span>
};

export default TextDisp;