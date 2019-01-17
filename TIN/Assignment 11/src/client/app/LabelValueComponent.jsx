import React from 'react';

const LabelValue = function(props){
    return <div className={props.class}>{props.label} : {props.val}</div>
};

export default LabelValue;