<?php
return [
    "_" => function() {
        return array(
            new \Monolog\Handler\StreamHandler(__DIR__ . '/logs/' . 'errors.log', \Monolog\Logger::ERROR),
        );
    }
];