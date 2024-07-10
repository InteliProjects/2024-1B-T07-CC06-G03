import { createContext } from "react";

export const DataSharingContext = createContext();

export const DataSharingProvider = ({ children }) => {
  return (
    <DataSharingContext.Provider value={{}}>
      {children}
    </DataSharingContext.Provider>
  );
};
