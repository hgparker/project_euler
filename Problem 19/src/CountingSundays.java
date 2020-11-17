public class CountingSundays {

    public CountingSundays() {
        // offset mod 7 by month for nonLY and LY
        short[] nonLeapYearMonthlyOffsets = new short[12];
        short[] leapYearMonthlyOffsets = new short[12];
        // number of 1st Sundays for nonLY / LY depending Jan 1st mod 7
        short[] nonLeapFirstSundays = new short[7];
        short[] leapFirstSundays = new short[7];

        short day;

        //All months default
        for (int k = 0; k < 12; k++)
            nonLeapYearMonthlyOffsets[k] = leapYearMonthlyOffsets[k] = 3;
        //February
        nonLeapYearMonthlyOffsets[1] = 0;
        leapYearMonthlyOffsets[1] = 1;
        //September, April, June, and November
        nonLeapYearMonthlyOffsets[8] = nonLeapYearMonthlyOffsets[3] = nonLeapYearMonthlyOffsets[5] = nonLeapYearMonthlyOffsets[10] = 2;
        leapYearMonthlyOffsets[8] = leapYearMonthlyOffsets[3] = leapYearMonthlyOffsets[5] = leapYearMonthlyOffsets[10] = 2;

        //Calculate nonLeapFirstSundays
        for (short k = 0; k < 7; k++) {
            nonLeapFirstSundays[k] = 0;
            day = k;
            for (int p = 0; p < 12; p++) {
                if (day == 6)
                    nonLeapFirstSundays[k]++;
                day += nonLeapYearMonthlyOffsets[p];
                day %= 7;
            }
        }

        //Calculate LeapFirstSundays
        for (short k = 0; k < 7; k++) {
            leapFirstSundays[k] = 0;
            day = k;
            for (int p = 0; p < 12; p++) {
                if (day == 6)
                    leapFirstSundays[k]++;
                day += leapYearMonthlyOffsets[p];
                day %= 7;
            }
        }

        short nonLeapTotalOffset = 0;
        short leapTotalOffset = 0;

        for (int k = 0; k < 12; k++) {
            nonLeapTotalOffset += nonLeapYearMonthlyOffsets[k];
            nonLeapTotalOffset %= 7;
            leapTotalOffset += leapYearMonthlyOffsets[k];
            leapTotalOffset %= 7;
        }

        short totalCount = 0;
        day = nonLeapTotalOffset;
        for (short year = 1901; year < 2001; year++) {
            if (isLeapYear(year)) {
                totalCount += leapFirstSundays[day];
                day += leapTotalOffset;
                day %= 7;
            } else {
                totalCount += nonLeapFirstSundays[day];
                day += nonLeapTotalOffset;
                day %= 7;
            }
        }

        System.out.println(totalCount);
    }

    private boolean isLeapYear(short n) {
        if (n % 400 == 0)
            return true;
        else if (n % 100 == 0)
            return false;
        else if (n % 4 == 0)
            return true;
        else
            return false;
    }

    public static void main(String[] args) {
        CountingSundays test = new CountingSundays();
    }
}
