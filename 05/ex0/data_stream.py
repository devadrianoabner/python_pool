#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any, typing


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: list[str] = []
        self._rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        try:
            value = self._data.pop(0)
            current_rank = self._rank
            self._rank += 1
            return (current_rank, value)
        except IndexError:
            raise ValueError("No data to output")


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, int | float):
            return True
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, int | float):
                    return False
            return True
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            for item in data:
                self._data.append(str(item))
        else:
            self._data.append(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, str):
                    return False
            return True
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            for item in data:
                self._data.append(item)
        else:
            self._data.append(data)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return self._valid_log(data)
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, dict):
                    return False
                if not self._valid_log(item):
                    return False
            return True
        return False

    def _valid_log(self, log: dict[Any, Any]) -> bool:
        for key, value in log.items():
            if not isinstance(key, str):
                return False
            if not isinstance(value, str):
                return False
        return "log_level" in log and "log_message" in log

    def ingest(self, data: dict[str, str]
               | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        if isinstance(data, list):
            for log in data:
                self._data.append(self._format(log))
        else:
            self._data.append(self._format(data))

    def _format(self, log: dict[str, str]) -> str:
        return f"{log['log_level']}: {log['log_message']}"
    
    def process_stream(self, stream: list[typing.Any]) -> None:
        for element in stream:
            handled = False
            for proc in self.processors:
                if proc.validate(element):
                    proc.ingest(element)
                    handled = True
                    break
            if not handled:
                print("DataStream error - Can't process element ", 
                      f"in stream: {element}")
