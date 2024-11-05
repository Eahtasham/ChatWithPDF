//Will handle the list of questins and ansewr and map  them to the correct question and answer/

import React from 'react';

const AnswerList = ({ qaList }) => {
  return (
    <div className="flex flex-col-reverse space-y-4">
      {qaList.map((item, index) => (
        <div key={index} className="bg-white p-6 rounded-lg shadow-md">
          <div className="mb-2">
            <h3 className="font-semibold text-gray-800">Q: {item.question}</h3>
          </div>
          <div className="pl-4 border-l-2 border-green-500">
            <p className="text-gray-600">A: {item.answer}</p>
          </div>
        </div>
      ))}
    </div>
  );
};

export default AnswerList;
