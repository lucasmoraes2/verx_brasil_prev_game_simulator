CREATE TABLE IF NOT EXISTS players (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    balance INT DEFAULT 300,
    behavior_type VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS properties (
    id SERIAL PRIMARY KEY,
    cost INT,
    rent INT,
    owner_id INT REFERENCES players(id)
);

INSERT INTO players (name, balance, behavior_type) VALUES
    ('Player 1', 300, 'impulsive'),
    ('Player 2', 300, 'demanding'),
    ('Player 3', 300, 'cautious'),
    ('Player 4', 300, 'random')
    ON CONFLICT DO NOTHING;

INSERT INTO properties (cost, rent, owner_id) VALUES
(100, 10, NULL),
(150, 15, NULL),
(200, 20, NULL),
(250, 25, NULL),
(300, 30, NULL),
(350, 35, NULL),
(400, 40, NULL),
(450, 45, NULL),
(500, 50, NULL),
(550, 55, NULL),
(600, 60, NULL),
(650, 65, NULL),
(700, 70, NULL),
(750, 75, NULL),
(800, 80, NULL),
(850, 85, NULL),
(900, 90, NULL),
(950, 95, NULL),
(1000, 100, NULL),
(1050, 105, NULL);
