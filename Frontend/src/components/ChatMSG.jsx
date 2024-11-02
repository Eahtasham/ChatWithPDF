import React from 'react'

export const ChatMSG = ({message,type}) => {
  return (
    <div className={`flex ${type==="user"? 'justify-end':'justify-start'} mb-4`}>
        <div className={`max-w-[70%] rounded-lg p-4 ${type==="user"
            ? 'bg-green-700 text-white rounded-br-none'
            : 'bg-gray-100 text-gray-800 rounded-bl-none'
        }
            
            `}> 
            {message}
        </div>

    </div>
  )
}