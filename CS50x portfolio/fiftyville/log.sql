-- Keep a log of any SQL queries you execute as you solve the mystery.

-- (1) I first accessed desciption text in the table crime scene report in order to get more information
--      So, first query was : SELECT description FROM crime_scene_reports WHERE day= 28 AND month=7 AND year =2021
--      AND street= "Humphrey Street";
--
-- (2) I did a second query in table bakery security logs to know acitivity text column at the time given.
--      first attempt of query:
--      SELECT activity FROM bakery_security_logs WHERE hour= 10
--      AND minute= 15 AND day= 28 AND month= 7 AND year = 2021;

--      second attempt query: SELECT * FROM bakery_security_logs WHERE hour= 16
--      AND minute= 36 AND day= 27 AND month= 7 AND year = 2021;
--      information of person who went to do littering with car is: id =207, activity: exit, license plate: X4G3938

-- (3)                                   query of interviews:
--       SELECT * FROM interviews WHERE day= 28 AND month = 7 AND year= 2021;
--      flight tickets on 29/07/2021; bakery secuirity logs: within 10 minutes of 10:15.

-- (4)                          query for finding vechicle registration plate:
--
--      SELECT * FROM bakery_security_logs WHERE hour= 10 AND minute >=15 AND minute <= 25 AND day= 28 AND month= 7 AND year= 2021;


-- (5)                                    query in phone calls:
--      SELECT * FROM phone_calls WHERE day= 28 AND month= 7 AND year = 2021 AND duration <= 60;

-- (6)  query to find thief
--                                              FINDING THIEF
--                    (BY intersecting phone calls,license plate, account number and flight elements)
--

--      SELECT * FROM people WHERE passport_number IN(
--      SELECT passport_number FROM passengers WHERE flight_id IN(
--      SELECT id FROM flights WHERE origin_airport_id =
--      (SELECT id FROM airports WHERE city ="Fiftyville") AND day= 29 AND month= 7 AND year= 2021 AND hour <= 9 AND hour >= 1 )
--      INTERSECT
--      SELECT passport_number FROM people WHERE id IN (
--      SELECT person_id FROM bank_accounts WHERE account_number IN(
--      SELECT account_number FROM atm_transactions WHERE day= 28 AND month= 7 AND year = 2021 AND atm_location= "Leggett Street"
--      AND transaction_type LIKE "%withdraw%")
--      INTERSECT
--      SELECT id FROM people WHERE license_plate IN(
--      SELECT license_plate FROM bakery_security_logs WHERE hour= 10 AND minute >=15 AND minute <= 25 AND day= 28 AND month= 7 AND year= 2021
--      INTERSECT
--      SELECT license_plate FROM people WHERE phone_number IN
--      (SELECT caller FROM phone_calls WHERE day= 28 AND month= 7 AND year = 2021 AND duration <= 60
--      INTERSECT
--      SELECT phone_number FROM people))));

--(7)                       QUERY FOR FINDING ACCOMPLICE

--      SELECT name FROM people WHERE phone_number=(
--      SELECT receiver FROM phone_calls WHERE caller LIKE "%(367) 555-5533%" AND day=28 AND month= 7 AND year= 2021 AND duration <= 60);

-- (8)                      QUERY FOR FINDING CITY OF ARRIVAL
--      SELECT city FROM airports WHERE id=
--      (SELECT destination_airport_id FROM flights WHERE id=
--      (SELECT flight_id FROM passengers WHERE passport_number = 5773159633));