let Suman = (number) => {
  let result = 0;
  let temp = number;
  while (temp > 0) {
    result = result * 10 + (temp % 10);
    temp = Math.floor(temp / 10);
  }
  return number === result;
};
