import React from "react";
import OpenAIChatBox from "./ui/OpenAIChatBox";

const page = () => {
  return (
    <div>
      <h2 className="scroll-m-20 border-b py-1 pt-20  text-4xl md:text-5xl font-semibold tracking-tight first:mt-0 w-fit mx-4 max-w-4xl">
        Wandering Travel Agent 
      </h2>
      <OpenAIChatBox />
    </div>
  );
};

export default page;
